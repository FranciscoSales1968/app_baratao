import curses

def main(stdscr):
    # Limpa a tela
    stdscr.clear()
    
    # Esconde o cursor
    curses.curs_set(0)
    
    # Define o título e as opções do menu
    title = "BARATÃO - AUTOPEÇAS"
    menu = ["1. Segurança", "2. Configuração", "3. Movimentação", "4. Relatório", "5. Backup e Restore", "6. Sair"]

    # Função para exibir o menu
    def display_menu(stdscr, selected_row_idx):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        x = w//2 - len(title)//2
        stdscr.addstr(1, x, title, curses.A_BOLD)
        
        for idx, row in enumerate(menu):
            x = w//2 - len(row)//2
            y = h//2 - len(menu)//2 + idx
            if idx == selected_row_idx:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
        stdscr.refresh()

    # Inicializa as cores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row = 0
    display_menu(stdscr, current_row)

    while True:
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == ord('\n'):
            if current_row == len(menu) - 1:
                break
            stdscr.addstr(0, 0, f"Você selecionou '{menu[current_row]}'", curses.A_REVERSE)
            stdscr.refresh()
            stdscr.getch()
        
        display_menu(stdscr, current_row)

    # Finaliza o curses
    stdscr.clear()
    stdscr.refresh()

curses.wrapper(main)
