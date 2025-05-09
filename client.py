import grpc 
import src.assistant_pb2 as pb2
import src.assistant_pb2_grpc as pb2_grpc



def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = pb2_grpc.AssistantServiceStub(channel)

    session_id= "test_session"

    print("Type 'exit' to stop chatting." )
    
    while True:
        user_input =input("You: ")
        if user_input.lower() == "exit":
            break
            
        request = pb2.UserMessage(session_id=session_id, user_input=user_input)

        response = stub.SendMessage(request)

        print("AI:",response.reply)
        print("Context so far:", list(response.context))
        print("--"*40)


    

if __name__ == "__main__":
    run()
