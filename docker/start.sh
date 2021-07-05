#!/usr/bin/env bash
MANAGE_PARAM=""

if [ -z "$APP_ENV" ]; then
    MANAGE_PARAM="--settings=poke_challenge.settings"
else
    if [ "$APP_ENV" = "DEV" ]; then
        MANAGE_PARAM='--settings=poke_challenge.settings.dev'
    elif [ "$APP_ENV" = "PROD" ]; then
        MANAGE_PARAM='--settings=poke_challenge.settings.prod'
    fi
fi


cd poke_challenge

poetry run python3 manage.py migrate $MANAGE_PARAM
poetry run python3 manage.py collectstatic --no-input $MANAGE_PARAM
poetry run python3 manage.py runserver 0.0.0.0:8000 $MANAGE_PARAM
