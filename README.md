# Your Project's Name

The Issue Tracker project is a public facing app.  Allowing a user to log bugs and request new features for their given app.
The app has alow a dev facing component which allows a dev to accept / reject which ticket they would like to work on, and update tickets.
 
## UX

UX wireframes located in /planning/wireframes
There was some minor changes in the final UI to allow for solutions for certain bugs and defects. There is a image of colors.io for the UI color scheme.

User stories located in /planning/user_stories
They describe some basic actions and featur for users in the app. 

We have a high level scope doc o help plan out tickets and User Stories



## Features

As a user they can
- create new bugs
- create new featues
- view comments on a tickey
- add a new comment
- up-vote a bug or a feature
- submit a payment via stripe
- use the contact us open to contact the dev team

as a dev they can
- log in as a dev user
- create new bugs
- create new featues
- view comments on a tickey
- add a new comment
- up-vote a bug or a feature
- accept or reject a ticket for work.
- update a tickets status and close it if needed.

### Features Left to Implement
- Date filter by date.
- Search by ticket id.
- pagination on dashboard
- add UI driven testing via Selenium (https://www.guru99.com/selenium-python.html)

## Technologies Used

- [HTML]
    - Was used to build the main pages.

- [CSS]
    - custom styling of pages.

- [JQuery]
    - used for some interactive elemens on forms and to hide some fields.

- [JaveScript]
    - as part of JQuery.

- [Bootstrap]
    - for the main styling template.

- [Django v1.11]
    - for serving webpages to users and interfacting with the DB.

- [Python 3]
    - as part of Django.

- [SQLite3]
    - Used on the local build of the app for testing.

- [PostgreSQL]
    - Used on the live version of the app.

- [Heroku]
    - Hosting the live app.

- [GIT]
    - For version control while developing.

- [GitHub]
    - project files hosted here.

- [Amazon Web Services / S3]
    - for serving static files and media files.

- [Stripe]
    - for payment processing

- [Trello]
    - https://trello.com/b/aKFZcGf5/issuetracker
    - Usedd to plan and manage work


## Testing

Tests are out lined in the user stories.  They are used for manual testing and will be used as part of creating Selenium testing via pythong in a later sprint.

## Deployment

Reused Code: The accounts sections was inported from an older project.  Large sections where striped out as they where not requried for this project and other areas where altered as needed.

All other cide is orginal.

Imported information like secret keys and other environment variables are hidden from the app.  Installing the app locally  will require an env file which needs to be provided seperatly.  With out this the app will not run locally.

No aditional changes are required to run the app on a live environment.

The app itself it devided into different apps, which are named after the behaviore held withint each app.
- accounts
- contact_us
- dashboard
- dev_area
- issue_tracker (project app)
- tickets

## Credits

### Content
No text or information was copied from external sources.

### Media
No media from external sources where used.

### Acknowledgements

No Acknowledgements are required