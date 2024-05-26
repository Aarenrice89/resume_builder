from builder.utils.const import L1, L2


def handle_bulled_list(list_data: list[str]) -> str:
    s = ""
    s += f"{L1}\\explanationdetail{'{'}\n"
    for x in list_data:
        s += f"{L2}\\smallskip\n"
        s += f"{L2}\\coloredbullet\\ %\n"
        s += f"{L2}{x}\n"
        s += f"{L2}\n"
    s += f"{L1}{'}'}\n"
    return s
