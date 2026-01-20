import asyncio
from BkLightToolkit.api import Panel, PanelManager

async def main():
    panel1 = Panel("AA:BB:CC:DD:EE:FF")
    panel2 = Panel("11:22:33:44:55:66")

    manager = PanelManager([panel1, panel2])

    await manager.send("Hello World", color=(255, 0, 0))

    await manager.send("test.png")

if __name__ == "__main__":
    asyncio.run(main())
