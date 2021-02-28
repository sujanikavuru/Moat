import time
from pageObjects.MoatHomepage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
from utilities import XlUtils


class Test_002_DDT_HomePage:
    baseURL = ReadConfig.getApplicationURl()
    # search_input = ReadConfig.getSearchInput()
    path = "./TestData/search.xlsx"
    logger = LogGeneration.loggen()
    random_list = []
    status_testcase = []

    def test_homePageTittle(self, setup):
        self.logger.info("***Test_002_DDT_HomePage****")
        self.logger.info("***Verify Homepage title****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sb = HomePage(self.driver)
        time.sleep(5)
        actual_title = self.driver.title
        if actual_title == "Measurement, Analytics, & Brand Safety | Moat by Oracle Data Cloud":
            assert True
            self.logger.info("*** Homepage title verified successfully****")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_homePageTittle.png")
            self.logger.info("*** Homepage title verification  Failed****")
            self.driver.close()
            assert False

    def test_searchBrand(self, setup):
        self.logger.info("***Test_001_HomePage****")
        self.logger.info("***Test_001_HomePage****")
        self.logger.info("***Verify Search brand****")
        self.driver = setup
        self.rows = XlUtils.getRowCount(self.path, 'Search1')
        for row in range(2, self.rows + 1):
            self.search_1 = XlUtils.readData(self.path, 'Search1', row, 1)
            self.driver.get(self.baseURL)
            self.sb = HomePage(self.driver)
            self.sb.searchBrand(self.search_1)
            self.sb.selectBrand(self.search_1)
            cc, cac = self.sb.creativecount()
            self.logger.info("*** Creatives generated ****" + str(cc[0]))
            self.logger.info("*** Ads generated matched ****" + str(len(cac)))
            if len(cac) == int(cc[0]):
                assert True
                self.status_testcase.append("Pass")
                self.logger.info("*** Creatives generated and ads generated matched correctly****")
            else:
                self.status_testcase.append("Fail")
                self.logger.info("*** Creatives generated and ads generated mismatched ****")
                self.logger.info("*** Failed as the Creatives generated and ads generated mismatched ****")
                assert False
            txt = self.sb.randomBrand()
            self.random_list.append(txt)
            self.logger.info("*** random brand first****" + str(self.random_list))
            txt1 = self.sb.randomBrand()
            self.logger.info("*** random brand second****" + str(txt1))
            if txt1 not in self.random_list:
                self.logger.info("*** Random link generates random data ****")
                assert True
            else:
                self.driver.save_screenshot("./Screenshots/" + "test_searchBrand.png")
                self.logger.info("*** Random link generates same content everytime ****")
                self.logger.error("*** Random link Failed to generate random content****")
                self.driver.close()
                assert False, "random link generates same content"
            self.sb.adsCheck()
            self.sb.verifyShare()
        if "Fail" not in self.status_testcase:
            self.logger.info("*** search test case is passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** search test case is failed ****")
            self.driver.close()
            assert False
        self.logger.info("*** End of Test ****")
