from behave import given, when, then
from selenium import webdriver
from utils import Utils
from pages.header_page import HeaderPage
from nose.tools import assert_equal
from pages.results_page import ResultsPage

utils = Utils()
header_page = HeaderPage()
results_page = ResultsPage()

@given(u'que acesso o site python')
def step_impl(context):
    utils.navegar("https://www.python.org/")


@given(u'preencho o input de pesquisa')
def step_impl(context):
    header_page.preencher_input_busca('python')


@when(u'clico no botão de pesquisa')
def step_impl(context):
    header_page.click_btn_go()

@then(u'devo visualizar os resultados da pesquisa')
def step_impl(context):
    assert_equal(results_page.get_text_title(), 'Search Python.org')
