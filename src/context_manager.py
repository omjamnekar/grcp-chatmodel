from src.mcp_message import MCPMessage

class ContextManager:
    def __init__(self):
        self.context = {}

    def update_context(self, session_id, user_input, model_response):
        if session_id not in self.context:
            self.context[session_id] = []
        self.context[session_id].append(MCPMessage("user", user_input))
        self.context[session_id].append(MCPMessage("assistant", model_response))


    def get_context(self, session_id):
        return [msg.to_dict() for msg in self.context.get(session_id, [])]

    
