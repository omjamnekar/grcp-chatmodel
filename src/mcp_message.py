# mcp_message.py
class MCPMessage:
    def __init__(self, role, content):
        self.role = role  # 'user', 'assistant'
        self.content = content

    def to_dict(self):
        return {"role": self.role, "content": self.content}

    @staticmethod
    def from_dict(data):
        return MCPMessage(role=data["role"], content=data["content"])
