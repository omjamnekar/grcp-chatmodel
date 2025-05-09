import grpc
from concurrent import futures
import src.assistant_pb2 as pb2
import src.assistant_pb2_grpc as pb2_grpc

from src.context_manager import ContextManager
import google.generativeai as genai  
import os
from dotenv import load_dotenv


load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API"))
model = genai.GenerativeModel("gemini-1.5-flash")

class AssistantService(pb2_grpc.AssistantServiceServicer):
    def __init__(self):
        self.context_manager = ContextManager()

    def SendMessage(self, request, context):
        session_id = request.session_id
        user_input = request.user_input

        structured_context = self.context_manager.get_context(session_id)

        prompt = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in structured_context])
        prompt += f"\nUser: {user_input}"

        try:
            response = model.generate_content(prompt)
            ai_reply = response.text.strip()
        except Exception as e:
            ai_reply = f"[Gemini Error: {str(e)}]"


        self.context_manager.update_context(session_id, user_input, ai_reply)

        updated_context = self.context_manager.get_context(session_id)
        return pb2.ModelResponse(reply=ai_reply, context=[f"{m['role'].capitalize()}: {m['content']}" for m in updated_context])
  



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_AssistantServiceServicer_to_server(AssistantService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Server with Gemini started on port 50051.")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
