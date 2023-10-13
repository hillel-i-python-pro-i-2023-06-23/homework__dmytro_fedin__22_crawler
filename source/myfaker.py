from faker import Faker


fake = Faker()

fake_name = fake.name()


def print_fake_name() -> None:
    print(f"My name is {fake_name}.")
