from django.test import TestCase
from django.shortcuts import resolve_url as r


class ServiceWorkerTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('serviceworker'))

    def test_get(self):
        """GET /serviceworker.js Should return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_serviceworker_renders(self):
        """Must render template tag"""
        contents = [
            "'/offline/',",
            "'/static/images/icons/icon-72x72.png',",
            "'/static/images/icons/icon-96x96.png',",
            "'/static/images/icons/icon-128x128.png',",
            "'/static/images/icons/icon-144x144.png',",
            "'/static/images/icons/icon-152x152.png',",
            "'/static/images/icons/icon-192x192.png',",
            "'/static/images/icons/icon-384x384.png',",
            "'/static/images/icons/icon-512x512.png',",
            "'/static/images/icons/splash-640x1136.png',",
            "'/static/images/icons/splash-750x1334.png',",
            "'/static/images/icons/splash-1242x2208.png',",
            "'/static/images/icons/splash-1125x2436.png',",
            "'/static/images/icons/splash-828x1792.png',",
            "'/static/images/icons/splash-1242x2688.png',",
            "'/static/images/icons/splash-1536x2048.png',",
            "'/static/images/icons/splash-1668x2224.png',",
            "'/static/images/icons/splash-1668x2388.png',",
            "'/static/images/icons/splash-2048x2732.png'",
            "return caches.match('/offline/')"
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)



class ManifestTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('manifest'), format='json')

    def test_get(self):
        """GET /manifest.json Should return status code 200"""
        self.assertEqual(self.response.status_code, 200)

    def test_content_type_json(self):
        """The content type Must be JSON"""
        self.assertEqual(self.response['content-type'], 'application/json')

    def test_template(self):
        """Must have the template manifest.json"""
        self.assertTemplateUsed(self.response, 'manifest.json')

    def test_manifest_contains(self):
        """Must be the attributes to manifest.json"""
        contents = [
            '"name":',
            '"short_name":',
            '"description":',
            '"start_url":',
            '"display":',
            '"scope":',
            '"background_color":',
            '"theme_color":',
            '"orientation":',
            '"icons":',
            '"dir":',
            '"lang":',
            '"status_bar":'
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_icons_path_renders(self):
        """Must render template tag"""
        self.assertEqual(self.response.json()['icons'], [
            {
                'src': '/static/images/icons/icon-72x72.png',
                'size': '72x72'
            },
            {
                'src': '/static/images/icons/icon-96x96.png',
                'size': '96x96'
            },
            {
                'src': '/static/images/icons/icon-128x128.png',
                'size': '128x128'
            },
            {
                'src': '/static/images/icons/icon-144x144.png',
                'size': '144x144'
            },
            {
                'src': '/static/images/icons/icon-152x152.png',
                'size': '152x152'
            },
            {
                'src': '/static/images/icons/icon-192x192.png',
                'size': '192x192'
            },
            {
                'src': '/static/images/icons/icon-384x384.png',
                'size': '384x384'
            },
            {
                'src': '/static/images/icons/icon-512x512.png',
                'size': '512x512'
            }
        ])


class OfflineTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('offline'))

    def test_get(self):
        """GET /offline Should return status code 200"""
        self.assertEqual(200, self.response.status_code)

