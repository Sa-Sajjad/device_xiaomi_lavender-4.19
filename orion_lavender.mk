#
# Copyright (C) 2018-2019 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common OrionOS stuff
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from lavender device
$(call inherit-product, $(LOCAL_PATH)/device.mk)

# OrionOS stuff
ORION_MAINTAINER := Sajjad
ORION_MAINTAINER_LINK := https://t.me/sa_sajjadx
TARGET_ENABLE_BLUR := true
TARGET_BOOT_ANIMATION_RES := 1080

# Common flags
# ORION_GAPPS := true
# BUILD_GOOGLE_CONTACTS := true
# BUILD_GOOGLE_DIALER := true
# BUILD_GOOGLE_MESSAGE := true

PRODUCT_NAME := orion_lavender
PRODUCT_BRAND := Xiaomi
PRODUCT_DEVICE := lavender
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_MODEL := Redmi Note 7

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi
TARGET_VENDOR_PRODUCT_NAME := lavender
