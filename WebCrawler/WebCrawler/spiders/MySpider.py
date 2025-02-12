import scrapy


class MyspiderSpider(scrapy.Spider):
    name = 'MySpider'
    allowed_domains = ['mstajbakhsh.ir']

    start_urls = [  "https://mstajbakhsh.ir/",
                    "https://mstajbakhsh.ir/page/2",
                    "https://mstajbakhsh.ir/page/3",
                    "https://mstajbakhsh.ir/page/4",
                    "https://mstajbakhsh.ir/page/5",
                    "https://mstajbakhsh.ir/page/6" ]


    def parse(self, response):
        for link in response.xpath("/html/body/div//article/header/a/@href").getall():
            yield scrapy.Request(url = link, dont_filter=True, callback=self.PageParser)  

    

    def PageParser(self,response):
        category1 = response.xpath("//ul[@class='post-category']/li[1]/a/text()").get()

        body = "".join(response.xpath("/html/body//article/div[3]//text()").getall())
        yield {
            'category1':category1,
            'body':body
        }