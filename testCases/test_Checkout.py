import time
from pageObjects.CheckoutPage import CheckoutPage


class Test_Checkout:

    baseURL = "https://newapp-staging.qlub.cloud/qr/ae/dummy-checkout/90/_/_/1827c10c80"
    cardNumber = "4242424242424242"
    expiryDate = "0226"
    cvv = "100"

    def test_checkoutPageTitle(self, setup):

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        time.sleep(3)
        act_title = self.driver.title

        if act_title == "Qlub_ | dummy-checkout":
            assert True
            self.driver.quit()

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_payNowPage.png")
            self.driver.quit()
            assert False

    def test_completePay(self, setup):

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.cp = CheckoutPage(self.driver)
        self.cp.clickPayNowButton()
        self.cp.clickSplitBillButton()
        self.cp.clickSelectButton()
        self.cp.setAmount("20")
        self.cp.selectTip()
        self.cp.enterCardInformation(self.cardNumber, self.expiryDate, self.cvv)
        self.cp.clickPayNowButton2()
        message = self.cp.messageText()

        if message == "Payment was successful!":
            self.driver.quit()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_cardInformationPage.png")
            self.driver.quit()
            assert False
