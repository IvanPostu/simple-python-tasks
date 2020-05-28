from password_manager.PasswordGenerator import PasswordGenerator


def test_PasswordGenerator():
    letter_count = 3
    num_count = 4
    symb_count = 7
    pass_gen = PasswordGenerator(letter_count, num_count, symb_count)
    generated_password = pass_gen.generate()
    assert len(generated_password) == letter_count + num_count + symb_count
