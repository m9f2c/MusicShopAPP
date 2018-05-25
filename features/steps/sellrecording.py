from behave import *

use_step_matcher("parse")


@given('Add sell recording: by "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)


@Given('Create and login by "{username}" width password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/accounts/login/'))
    form = context.browser.find_by_tag('form').first

    context.browser.fill('username', username)
    context.browser.fill('password', password)

    form.find_by_css('button').first.click()

@then('View user "{username}" workspace and "{password}"')
def step_impl(context, username, password):
    from PersonalPage.models import User_Recording_Sell
    from MusicShop.models import Artist
    from MusicShop.models import Recording

    context.browser.visit(context.get_url('/personal_page/sell_recording'))

    form = context.browser.find_by_tag('form').first

    for row in context.table:
        sell_recording = User_Recording_Sell()

        for heading in row.headings:
            if heading == "artist":
                artist = Artist()
                artist.name = row[heading]
                sell_recording.artist = artist

            if heading == "recording":
                recording = Recording()
                recording.title = row[heading]
                sell_recording.recording = recording

            if heading == "description":
                sell_recording.description = row[heading]

            if heading == "price":
                sell_recording.price = row[heading]

        context.browser.fill('Artist', str(sell_recording.artist))
        context.browser.fill('Recording', str(sell_recording.recording))
        context.browser.fill('Desc', str(sell_recording.description))
        context.browser.fill('Price', str(sell_recording.price))
        form.find_by_css('button').first.click()


@then('There are {count:n} recording')
def step_impl(context, count):
    pass
    #from MusicShop.models import Artist
    #Artist count = Artist, str(sell_recording.artist)
    #assert count == Artist.objects.count(count)