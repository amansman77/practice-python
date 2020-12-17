import asyncio

async def inf_loop():
    loop_cnt = 0
    while loop_cnt < 5:
        print('loop is running, cnt:', loop_cnt)
        if loop_cnt == 2:
            await say('I am coroutine in inf_loop')
        loop_cnt += 1

async def say(what):
    print(what)

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    '''
    await의 대상이 코루틴이면 이벤트 루프에 넣지 않고 바로 실행한다는것에 대한 검즘을 해보는 코드입니다.

    flow 가정
    1. 태스크1을 동작한다.
    2. 태스크2를 이벤트루프에 추가한다.
    3. 태스크1에서 코루틴1-1을 await한다.
    4. 태스크2보다 코루틴1-1이 먼저 수행하면 해당 내용이 검증된다.
    '''
    print('create task1')
    task1 = asyncio.create_task(
        inf_loop()
    )

    print('create task2')
    task2 = asyncio.create_task(
        say_after(5, 'I will say after 5s')
    )

    print('await task1')
    await task1

    print('await task2')
    await task2

asyncio.run(main())