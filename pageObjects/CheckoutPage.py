import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    button_payNow_xpath = "//*[contains(@class, 'Vendor_priceContainer')]//*[@class='wrapper']"

    button_splitBill_xpath = "//*[text()='Split bill']"

    button_customAmountSelect_css = "#select-custom"

    textbox_amount_css = "#fullWidth"

    button_confirm_id = "split-bill"

    checkbox_tip_xpath = "//*[text()='10%']"

    textbox_cardNumber_css = "#checkout-frames-card-number"

    textbox_expiryDate_css = "#checkout-frames-expiry-date"

    textbox_cvv_css = "#checkout-frames-cvv"

    button_payNow2_xpath = "//*[text()='Pay Now']"

    text_messageInfo_xpath = "//*[text()='Payment was successful!']"

    def __init__(self, driver):
        self.driver = driver

    def clickPayNowButton(self):
        self.driver.find_element(By.XPATH,self.button_payNow_xpath).click()
        time.sleep(3)

    def clickSplitBillButton(self):
        self.driver.find_element(By.XPATH,self.button_splitBill_xpath).click()
        time.sleep(3)

    def clickSelectButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_customAmountSelect_css).click()
        time.sleep(3)

    def setAmount(self, amount):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_amount_css).send_keys(amount)
        self.driver.find_element(By.ID, self.button_confirm_id).click()
        time.sleep(3)

    def selectTip(self):
        self.driver.find_element(By.XPATH, self.checkbox_tip_xpath).click()

    def enterCardInformation(self, cardNumber, expiryDate, cvv):
        self.driver.switch_to.frame("checkout-frames-cardNumber")
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_cardNumber_css).send_keys(cardNumber)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.switch_to.frame("checkout-frames-expiryDate")
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_expiryDate_css).send_keys(expiryDate)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.switch_to.frame("checkout-frames-cvv")
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_cvv_css).send_keys(cvv)
        self.driver.switch_to.default_content()

    def clickPayNowButton2(self):
        self.driver.find_element(By.XPATH, self.button_payNow2_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.text_messageInfo_xpath)))

    def messageText(self):
        message = self.driver.find_element(By.XPATH, self.text_messageInfo_xpath).text
        time.sleep(2)
        return message