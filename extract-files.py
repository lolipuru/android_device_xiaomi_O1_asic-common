#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/o1_asic-common',
    'hardware/mediatek',
    'hardware/xiaomi',
    'vendor/xiaomi/o1_asic-common',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libcamlog',
        'com.xiaomi.camdfx'
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    (
        'odm/lib64/libmt_mitee.so',
        'vendor/bin/hw/android.hardware.security.keymint@3.0-service.mitee'
    ): blob_fixup()
        .replace_needed('android.hardware.security.keymint-V3-ndk.so', 'android.hardware.security.keymint-V3-ndk-xiaomi.so'),
}

module = ExtractUtilsModule(
    'o1_asic-common',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
    add_firmware_proprietary_file=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()