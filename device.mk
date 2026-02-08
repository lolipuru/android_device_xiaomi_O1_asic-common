#
# Copyright (C) 2024 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Call the proprietary setup.
$(call inherit-product, vendor/xiaomi/o1_asic-common/o1_asic-common-vendor.mk)

# Enable virtual AB with vendor ramdisk
$(call inherit-product, $(SRC_TARGET_DIR)/product/virtual_ab_ota/vabc_features.mk)

# Enable project quotas and casefolding for emulated storage without sdcardfs.
$(call inherit-product, $(SRC_TARGET_DIR)/product/emulated_storage.mk)

# Setup dalvik vm configs
$(call inherit-product, frameworks/native/build/phone-xhdpi-6144-dalvik-heap.mk)

# Enforce generic ramdisk allow list
$(call inherit-product, $(SRC_TARGET_DIR)/product/generic_ramdisk.mk)

# Rootdir
PRODUCT_PACKAGES += \
    fstab.O1_asic \
    fstab.O1_asic.vendor_ramdisk \
