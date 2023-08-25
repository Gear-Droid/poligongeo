from django.shortcuts import render
from django.views import View

from .models import CallRequest


class HomePageView(View):

    def get(self, request, *args, **kwargs):

        context = {
            'meta':{
                'Title': "Полигон ГЕО",
                'page_description': """
                    ООО «ПОЛИГОН ГЕО» основана в 2008 году. За время деятельности организации были успешно
                    выполнены изыскания и пройдена государственная экспертиза более чем 1500 объектов.
                    Главный принцип компании – высочайший уровень качества и строгое соблюдение сроков.
                    Благодаря многолетнему опыту работы, мы можем гарантировать первоклассный результат и
                    поручиться за каждый аспект выполняемых работ.
                    Компания выполняет изыскательские работы на объектах любой сложности,
                    включая те, которым присвоен статус «особо опасные, технически сложные и уникальные»
                """,
                'keywords': "",
            },
        }
        return render(request, 'homepage.html', context=context)

    def post(self, request, *args, **kwargs):
        firstName = request.POST.get('firstName')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        call_request = CallRequest.objects.create(first_name=firstName, phone=phone, email=email)

        context = {
            'meta':{
                'Title': "Полигон ГЕО",
                'page_description': """
                    ООО «ПОЛИГОН ГЕО» основана в 2008 году. За время деятельности организации были успешно
                    выполнены изыскания и пройдена государственная экспертиза более чем 1500 объектов.
                    Главный принцип компании – высочайший уровень качества и строгое соблюдение сроков.
                    Благодаря многолетнему опыту работы, мы можем гарантировать первоклассный результат и
                    поручиться за каждый аспект выполняемых работ.
                    Компания выполняет изыскательские работы на объектах любой сложности,
                    включая те, которым присвоен статус «особо опасные, технически сложные и уникальные»
                """,
                'keywords': "",
            },
        }
        return render(request, 'homepage.html', context=context)