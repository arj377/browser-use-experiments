from browser_use import Agent, Browser, ChatBrowserUse
import asyncio
import os

async def main():
    browser = Browser(headless=False)
    llm = ChatBrowserUse(api_key=os.environ["BROWSER_USE_API_KEY"])

    agent = Agent(
        task=(
            "Go to Depop. Search for men’s Curious George shirts. "
            "Filter for size small and price under $10. "
            "Find up to 4 matching listings. "
            "Return the item title, price, and link for each, "
            "then briefly summarize whether good options exist."
        ),
        llm=llm,
        browser=browser,
    )

    history = await agent.run()
    print(history.final_answer)

if __name__ == "__main__":
    asyncio.run(main())
