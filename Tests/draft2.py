
def name_b():
    s = "Hello World"
    txt = s[::-1]
    print(txt)


a = list(range(1, 5))
print(a)


def n(num):
    b = list(range(0, 14))
    c = f"[{b[num]}]"
    print(c)


n(0)


def reversed_string(a_string):
    return a_string[::-1]


FIRST_PAGE_JS = "return document.querySelector('array-account-enroll').shadowRoot.querySelector"
RADIO_BUTTON = "('array-authentication-kba').shadowRoot.querySelectorAll('.input.svelte-2s0uww')"
RADIO_OPTION = "('array-authentication-kba').shadowRoot.querySelectorAll('.label.svelte-2s0uww')"


def check_radio_button_value(page_js, radio_text_selector, radio_button_selector, num):
    b = list(range(0, 25))
    c0 = f"[{b[num]}]"
    c1 = f"[{b[num + 1]}]"
    c2 = f"[{b[num + 2]}]"
    c3 = f"[{b[num + 3]}]"
    c4 = f"[{b[num + 4]}]"
    rts = page_js + radio_text_selector
    rbs = page_js + radio_button_selector
    print(rts)
    print(rbs)
    print(rts + c0)
    print(rbs + c0)
    print(rts + c1)
    print(rbs + c1)


check_radio_button_value(FIRST_PAGE_JS, RADIO_OPTION, RADIO_BUTTON, 0)


