import time
from seleniumwire import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


def scan_watcher(address):
    try:
        print('start')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors-spki-list')
        chrome_options.add_argument('--ignore-ssl-errors')

        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

        driver.get(f'https://cryptowatchtower.io/tokens/scan/{address}/')
        time.sleep(50)
        value = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]').text
        final_result = value.split('/')[0]
        print(final_result)
        driver.quit()
        if int(final_result) >= 7:
            return True
        else:
            return False
    except NoSuchElementException:
        driver.quit()
        try:
            print('start')
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--ignore-certificate-errors-spki-list')
            chrome_options.add_argument('--ignore-ssl-errors')

            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

            driver.get(f'https://cryptowatchtower.io/tokens/scan/{address}/')
            time.sleep(50)
            value = driver.find_element_by_xpath(
                '//*[@id="__next"]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]').text
            final_result = value.split('/')[0]
            print(final_result)
            driver.quit()
            if int(final_result) >= 7:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            driver.quit()
    except Exception as e:
        driver.quit()
        print(e)
        return False


def scan_bs(address, network):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors-spki-list')
        chrome_options.add_argument('--ignore-ssl-errors')
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        if network == 'BSC':
            driver.get('https://www.bscheck.eu/bsc')
            input_adr = driver.find_element_by_xpath('//*[@id="it_contractNumber"]')
            input_adr.clear()
            input_adr.send_keys(address)
            time.sleep(10)
            driver.find_element_by_xpath('//*[@id="bt_check"]').click()
            time.sleep(20)
            result = driver.find_element_by_xpath('//*[@id="safescore_label"]').text
            if 'WARNING' in result:
                target_text = driver.find_element_by_xpath('//*[@id="report_honeypot"]').text
                result_tax = target_text.split('Honeypot.is report : Sell OK')[1]
                driver.quit()
                return ['WARNING', result_tax.replace('\n', '  ')]
            elif 'RISKY' in result:
                target_text = driver.find_element_by_xpath('//*[@id="report_honeypot"]').text
                result_tax = target_text.split('Honeypot.is report : Sell OK')[1]
                driver.quit()
                return ['RISKY', result_tax.replace('\n', '  ')]
            else:
                return False

        elif network == 'ETH':
            driver.get('https://www.bscheck.eu/eth')
            input_adr = driver.find_element_by_xpath('//*[@id="it_contractNumber"]')
            input_adr.clear()
            input_adr.send_keys(address)
            time.sleep(10)
            driver.find_element_by_xpath('//*[@id="bt_check_eth"]').click()
            time.sleep(20)
            result = driver.find_element_by_xpath('//*[@id="safescore_label"]').text
            if 'WARNING' in result:
                target_text = driver.find_element_by_xpath('//*[@id="report_honeypot"]').text
                result_tax = target_text.split('Honeypot.is report : Sell OK')[1]
                driver.quit()
                return ['WARNING', result_tax.replace('\n', '  ')]
            elif 'RISKY' in result:
                target_text = driver.find_element_by_xpath('//*[@id="report_honeypot"]').text
                result_tax = target_text.split('Honeypot.is report : Sell OK')[1]
                driver.quit()
                return ['RISKY', result_tax.replace('\n', '  ')]
            else:
                return False
    except Exception as e:
        print(e)
        driver.quit()
        return False


# print(scan_watcher('0x31903e333809897ee57af57567f4377a1a78756c'))
# print(scan_bs('0xcfe087ed979244db595e62a7bc1e01e6de6870e9', 'BSC'))

