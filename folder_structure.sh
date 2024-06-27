#!/bin/bash

# Define the base directory
BASE_DIR="."

# Create the folder structure and files
mkdir -p ${BASE_DIR}/core
touch ${BASE_DIR}/core/app.py
touch ${BASE_DIR}/core/config.py
touch ${BASE_DIR}/core/logger.py

mkdir -p ${BASE_DIR}/ui/layout
touch ${BASE_DIR}/ui/layout/main_layout.py

mkdir -p ${BASE_DIR}/ui/components
touch ${BASE_DIR}/ui/components/button.py
touch ${BASE_DIR}/ui/components/modal.py

mkdir -p ${BASE_DIR}/ui/styles
touch ${BASE_DIR}/ui/styles/themes.py

mkdir -p ${BASE_DIR}/features/auth
touch ${BASE_DIR}/features/auth/login.py
touch ${BASE_DIR}/features/auth/signup.py
touch ${BASE_DIR}/features/auth/profile.py

mkdir -p ${BASE_DIR}/features/dashboard
touch ${BASE_DIR}/features/dashboard/overview.py
touch ${BASE_DIR}/features/dashboard/widgets.py

mkdir -p ${BASE_DIR}/features/data_management
touch ${BASE_DIR}/features/data_management/data_entry.py
touch ${BASE_DIR}/features/data_management/data_display.py
touch ${BASE_DIR}/features/data_management/data_processing.py

mkdir -p ${BASE_DIR}/services/api
touch ${BASE_DIR}/services/api/api_service.py
touch ${BASE_DIR}/services/api/data_fetching.py

mkdir -p ${BASE_DIR}/services/database
touch ${BASE_DIR}/services/database/models.py
touch ${BASE_DIR}/services/database/repositories.py
touch ${BASE_DIR}/services/database/migrations.py

mkdir -p ${BASE_DIR}/services/notifications
touch ${BASE_DIR}/services/notifications/email.py
touch ${BASE_DIR}/services/notifications/push_notifications.py

mkdir -p ${BASE_DIR}/utils
touch ${BASE_DIR}/utils/helpers.py
touch ${BASE_DIR}/utils/validators.py

mkdir -p ${BASE_DIR}/integrations
touch ${BASE_DIR}/integrations/payment_gateway.py
touch ${BASE_DIR}/integrations/social_media.py

mkdir -p ${BASE_DIR}/tests/unit
touch ${BASE_DIR}/tests/unit/test_components.py

mkdir -p ${BASE_DIR}/tests/integration
touch ${BASE_DIR}/tests/integration/test_e2e.py

mkdir -p ${BASE_DIR}/deployment
touch ${BASE_DIR}/deployment/ci_cd_pipeline.py
touch ${BASE_DIR}/deployment/dockerfile

echo "Folder structure created successfully."
