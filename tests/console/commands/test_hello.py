from expanse.asynchronous.testing.command_tester import CommandTester


async def test_hello(command_tester: CommandTester) -> None:
    command = command_tester.command("hello")

    return_code: int = await command.run()

    assert return_code == 0
    assert command.output.fetch() == "Hello, World!\n"
