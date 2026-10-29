from pyscript import document, when

@when("click", "#enter-btn")
def candidate_checker(e):
    club_members = [
        "shawn tee", "eeeh tannnz", "kuh eye reen", 
        "zow fia kabig", "cler multo", "nzo.gpt", "silly vieya",
        "sophi ghey", "kehn jee", "xey uh riene", "ey vuhnd", 
    ]

    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name
    member_checker = candidate.title() in club_members

    messages = (
        f'Sorry {candidate}, your name is not on the list.', 
        f'Congratulations {candidate}! You are now part of the ICT Club!'
    )
    document.getElementById('result').innerHTML = messages[member_checker]
