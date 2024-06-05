from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def submit_solution(driver, solution_str):

    solution_box = get_solution_box(driver)
    enter_solution(solution_box, solution_str)
    

def enter_solution(solution_box, solution_str):

    solution_box.send_keys(solution_str)
    print(solution_str)
    input("hit enter to continue...")

    solution_box.send_keys(Keys.RETURN)


def get_solution_box(driver):

    solution_box = driver.find_element(By.NAME, "solution")

    return solution_box