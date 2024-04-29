import timeit

sample_text = """
Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime
mollitia, molestiae quas vel sint commodi repudiandae consequuntur
voluptatum laborum numquam blanditiis harum quisquam eius sed odit
fugiat iusto fuga praesentium optio, eaque rerum! Provident similique
accusantium nemo autem. Veritatis obcaecati tenetur iure eius earum
ut molestias architecto voluptate aliquam nihil, eveniet aliquid
culpa officia aut! Impedit sit sunt quaerat, odit, tenetur error,
harum nesciunt ipsum debitis quas aliquid.
"""
def char_frequency_lbyl(text):
    counter = {}
    for char in text:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter

def char_frequency_eafp(text):
    counter = {}
    for char in text:
        try:
            counter[char] += 1
        except KeyError:
            counter[char] = 1
    return counter


char_frequency_eafp(sample_text)


sample_text *= 100

eafp_time = min(
    timeit.repeat(
        stmt="char_frequency_eafp(sample_text)",
        number=1000,
        repeat=5,
        globals=globals(),
    )
)

lbyl_time = min(
    timeit.repeat(
        stmt="char_frequency_lbyl(sample_text)",
        number=1000,
        repeat=5,
        globals=globals(),
    )
)

print(f"LBYL is {lbyl_time / eafp_time:.3f} times slower than EAFP")
