import asyncio
from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentServer, AgentSession, Agent

load_dotenv(".env.local")


class VoiceAssistant(Agent):
    def __init__(self):
        super().__init__(
            instructions="""
You are a helpful voice AI assistant.

Rules:
- Speak naturally like ChatGPT voice.
- Keep responses short.
- Do not use markdown formatting.
- Do not use emojis.
- Respond conversationally.
"""
        )


server = AgentServer()


@server.rtc_session(agent_name="voice-agent")
async def handler(ctx: agents.JobContext):
    session = AgentSession(
        stt="deepgram/nova-3:multi",
        llm="openai/gpt-4.1-mini",
        tts="cartesia/sonic-3",
    )

    await session.start(
        room=ctx.room,
        agent=VoiceAssistant(),
    )

    await session.generate_reply(
        instructions="Greet the user and offer help."
    )


if __name__ == "__main__":
    agents.cli.run_app(server)