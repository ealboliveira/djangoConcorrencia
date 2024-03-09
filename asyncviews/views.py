import asyncio
import httpx
from django.http import HttpResponse
from django.views import View

class AsyncCallView(View):
    async def get(self, request):
        for num in range(1, 6):
            await asyncio.sleep(1)
            print(num)
        async with httpx.AsyncClient() as client:
            r = await client.get("https://httpbin.org")
            print(r)
        return HttpResponse("Async call complete")
