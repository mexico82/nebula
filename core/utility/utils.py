def build_menu(buttons, n_cols, header_buttons=False, footer_buttons=False):
  menu=[buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
  if header_buttons:
    menu.insert(0, header_buttons)
  if footer_buttons:
    menu.append(footer_buttons)
  return menu

class Colors:
  RED   = "\033[1;31m"  
  BLUE  = "\033[1;34m"
  CYAN  = "\033[1;36m"
  GREEN = "\033[0;32m"
  RESET = "\033[0;0m"
  BOLD    = "\033[;1m"
  REVERSE = "\033[;7m"