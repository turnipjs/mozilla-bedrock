# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from django.core.management.base import BaseCommand

from bedrock.sitemaps.utils import update_sitemaps


# Note that this command is only called by www-sitemap-generator, which uses the Docker image
# of Bedrock to regenerate sitemap data
class Command(BaseCommand):
    args = ""
    help = "Update XML sitemaps based on the list of localized pages."

    def handle(self, *args, **options):
        update_sitemaps()
