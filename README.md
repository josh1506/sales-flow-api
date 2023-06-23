# SalesFlow

SaleAnalytics is a powerful sales analytics platform designed to provide comprehensive insights into your sales data. It enables you to easily track and display sales information for various time periods such as 1 day, 7 days, 1 month, 1 year, and more. With SaleAnalytics, you can gain valuable visibility into your sales performance, identify trends, and make data-driven decisions to optimize your business strategy.

## Features

- **Flexible Sales Tracking:** SaleAnalytics allows you to track and aggregate sales data for different time frames, providing you with a clear overview of your sales performance.

- **Customizable Dashboards:** Create personalized dashboards tailored to your specific business needs. Choose the key metrics, charts, and visualizations you want to monitor and analyze.

- **Time Period Filters:** Effortlessly switch between different time periods to view sales data for 1 day, 7 days, 1 month, 1 year, and more. Gain insights into sales trends over time and identify patterns.

- **Visual Data Repgiresentation:** SaleAnalytics offers visually appealing charts, graphs, and reports to present your sales data in an easily understandable format. Get a clear snapshot of your sales performance at a glance.

- **User-Friendly Interface:** The intuitive and user-friendly interface of SaleAnalytics makes it easy to navigate, analyze data, and generate reports. You don't need to be a data expert to leverage the power of your sales information.

## Installation

To use SaleAnalytics, follow these steps:

1. Clone the repository: `git clone git@github.com:josh1506/sale-flow-api.git`

2. Start the application in your local: `sudo docker-compose -f local.yml up`

3. Access SaleAnalytics through your web browser at `http://localhost:8000` or `http://127.0.0.1:8000`.

## License

This project is licensed under the [MIT License](./LICENSE). You are free to modify and distribute the software for personal or commercial purposes.

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy salesflow

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd salesflow
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

```bash
cd salesflow
celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

```bash
cd salesflow
celery -A config.celery_app worker -B -l info
```

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
