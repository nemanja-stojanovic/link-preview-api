# link-preview-api

Preview links
I guess we all know what happens on Facebook when you paste an URL into a post?
Facebook's server automatically grabs the title, description, and picks a thumbnail image from the original website.
This API service is doing exactly that!

Server will inspect any requested URL and return JSON formatted summary with a title, description and preview image.
Bypassing same-origin policy is handled automatically.
