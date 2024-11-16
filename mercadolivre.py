import scrapy

class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino"]

    def parse(self, response):
        products = response.css('div.poly-card__content')
        #products = response.css('poly-component__variations')


        for product in products:

            yield {
                # LEVE STAR
                'brand': products.css('span.poly-component__brand::text').get(),
                #'brand': products.css(f'h2.{tenis}').get()

                # OLYMPIKUS
                #'name': products.css('ui-search-main ui-search-main--only-products.ui-search-main--with-topkeywords::text').get
            }


                