from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from login import login_to_hackthissite
from submit import submit_solution


def main():
    hts_words = []
    wordlist = []
    final_list = []

    driver = login_to_hackthissite()

    table = get_hts_table(driver)

    fill_hts_words(driver, table, hts_words)

    with open("wordlist.txt") as f:
        lines = f.readlines()

    fill_wordlist(lines, wordlist)

    get_matching_words(hts_words, wordlist, final_list)

    solution_str = ','.join(final_list)

    submit_solution(driver, solution_str)


def fill_wordlist(lines, wordlist):
    for line in lines:
        line.replace("\n", "")
        wordlist.append(line.replace("\n", ""))


def fill_hts_words(driver, table, hts_words):

    i = 1
    for li in table:
        li = driver.find_element(By.XPATH, f"/html/body/table/tbody/tr[2]/td/"
                                 + "table/tbody/tr/td[2]/table/tbody/tr[5]"
                                 + "/td[2]/table/tbody/tr[{i}]/td[2]/li")
        hts_words.append(li.text)
        i += 1


def strs_equal(word_1, word_2) -> bool:
    return len(word_1) == len(word_2)


def get_matching_words(hts_words, wordlist, final_list) -> None:

    wordlist_len = len(wordlist)

    for hts_word in hts_words:

        index = 0
        word_not_found = True

        while (index < wordlist_len) and word_not_found:

            current_wordlist_word = wordlist[index]
            words_same_len = strs_equal(hts_word, current_wordlist_word)

            if words_same_len:

                same_word = sort_and_compare(hts_word, current_wordlist_word)

                if same_word:

                    final_list.append(current_wordlist_word)
                    word_not_found = False

            index += 1


def sort_and_compare(str1, str2):
    same_word = sorted(str1) == sorted(str2)
    return same_word


def get_hts_table(driver):
    table_path = "/html/body/table/tbody/tr[2]/td/table/tbody/"
    + "tr/td[2]/table/tbody/tr[5]/td[2]/table/tbody/*"
    driver.implicitly_wait(10)
    table = driver.find_elements(By.XPATH, table_path)
    return table


if __name__ == "__main__":
    main()
