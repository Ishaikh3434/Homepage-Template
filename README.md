<h1>Homepage Template</h1>
This is a bare-bones but functional template homepage to organise Flask-based web projects. Designed to make it as easy as possible to add and remove projects, without requiring extensive changes to the layout of pre-existing projects using Flask's Blueprints.

Included is a template project that shows how a project should be formatted to add it to the homepage, but I'll also give a quick run-down here:

<h2>Formatting instructions</h2>
The overall structure requires a correctly-set-up project, and a corresponding entry in <i>/static/data/projects.json</i> ; the template should have enough info to guide you there. Additionally, a <i>.env</i> is required to hold the session key, as well as any other environment variables required by any other project (the session key is shared across all sub-projects, as are any other environment variables)

This system works by iterating over the <i>/projects</i> folder while looking for blueprints; as such, the <i><b>most important</b></i> thing to ensure is that the project has a blueprint defined in it's <i>\_\_init\_\_.py</i> ; this is the file that the top-level app is looking for, and the project will not be added if it isn't present.

Any routes for the project (such as API endpoints) should be defined in the routes.py file (required for every project, minimum is a '/' route for the "main page" of the project).

Finally, the thumbnails for each project should be kept in the <i>/static/img</i> folder, and referenced in <i>projects.json</i> by their <b><i>absolute path</i></b>.
