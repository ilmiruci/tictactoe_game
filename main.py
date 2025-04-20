import logging
from logging.handlers import RotatingFileHandler


def main():
    print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

    board = list(range(1, 10))

    def draw_board(board):
        try:
            print("-" * 13)
            for i in range(3):
                print(
                    "|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|"
                )
                print("-" * 13)
            logging.info("Доска обновлена")
        except Exception as err:
            logger.warning(err)

    def take_input(player_token):
        valid = False
        while not valid:
            player_answer = input("Куда поставим " + player_token + "? ")
            try:
                player_answer = int(player_answer)
                logger.info("Пользователь поставил %s в %s",player_token,player_answer)
            except Exception as err:
                print("Некорректный ввод. Вы уверены, что ввели число?")
                logger.info(err)
                continue
            if player_answer >= 1 and player_answer <= 9:
                if str(board[player_answer - 1]) not in "XO":
                    board[player_answer - 1] = player_token
                    valid = True
                else:
                    print("Эта клетка уже занята!")
                    logger.info("Попытка поставить в занятую клетку %s",player_answer)
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")


    def check_win(board):
        win_coord = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        )
        for each in win_coord:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
        return False

    def main(board):
        counter = 0
        win = False
        while not win:
            draw_board(board)
            if counter % 2 == 0:
                take_input("X")
            else:
                take_input("O")
            counter += 1
            if counter > 4:
                tmp = check_win(board)
                if tmp:
                    print(tmp, "выиграл!")
                    win = True
                    break
            if counter == 9:
                print("Ничья!")
                break
        draw_board(board)

    main(board)

    input("Нажмите Enter для выхода!")


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_handler = RotatingFileHandler(
        "my.log",
        mode="a",
        maxBytes=1 * 1024 * 1024,
        backupCount=2,
        encoding="UTF-8",
    )

    logger.addHandler(file_handler)

    logger_formatter = logging.Formatter(
        "[%(asctime)s.%(msecs)03d] %(module)-15s:%(lineno)-3d %(levelname)-7s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(logger_formatter)

    main()
