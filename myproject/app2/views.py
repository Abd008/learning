from django.http import HttpResponse

def vc(request, sentence):
    vow_cnt = 0
    cons_cnt = 0
    vow_dict = {}
    cons_dict = {}

    for letter in sentence:
        if letter.isalpha():
            if letter.lower() in "aeiou":
                vow_cnt += 1
                vow_dict[letter] = vow_dict.get(letter, 0) + 1
            else:
                cons_cnt += 1
                cons_dict[letter] = cons_dict.get(letter, 0) + 1

    result = f"<h1>{vow_cnt} Vowels and {cons_cnt} Consonants</h1>"

    result += "<h2>Vowel Counter</h2>"
    for key, value in vow_dict.items():
        result += f"<p>{key}: {value}</p>"

    result += "<h2>Consonant Counter</h2>"
    for key, value in cons_dict.items():
        result += f"<p>{key}: {value}</p>"

    return HttpResponse(result)