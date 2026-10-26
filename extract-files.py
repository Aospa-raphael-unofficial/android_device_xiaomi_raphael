#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

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
	'device/xiaomi/raphael',
	'vendor/xiaomi/raphael',
	'hardware/xiaomi',
	'vendor/qcom/common/system/alarm',
	'vendor/qcom/common/system/wfd',
	'vendor/qcom/common/system/telephony',
	'vendor/qcom/common/vendor/adreno-r',
	'vendor/qcom/common/vendor/display/4.14',
	'vendor/qcom/common/vendor/gps-legacy',
	'vendor/qcom/common/vendor/media/legacy',
	'vendor/qcom/common/vendor/qseecomd-legacy',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
	'libmmosal',
	'vendor.qti.hardware.wifidisplaysession@1.0',
	'vendor.qti.data.factory@2.0',
	'vendor.qti.data.factory@2.1',
	'vendor.qti.data.factory@2.2',
	'vendor.qti.data.factory@2.3',
	'vendor.qti.ims.rcsconfig@1.0',
	'vendor.qti.ims.rcsconfig@1.1',
	'vendor.qti.ims.rcsconfig@2.0',
	'vendor.qti.ims.rcsconfig@2.1',
	'vendor.qti.hardware.radio.ims@1.0',
	'vendor.qti.hardware.radio.ims@1.1',
	'vendor.qti.hardware.radio.ims@1.2',
	'vendor.qti.hardware.radio.ims@1.3',
	'vendor.qti.hardware.radio.ims@1.4',
	'vendor.qti.hardware.radio.ims@1.5',
	'vendor.qti.hardware.radio.ims@1.6',
	'vendor.qti.hardware.radio.ims@1.7',
	'com.qualcomm.qti.imscmservice@2.0',
	'com.qualcomm.qti.imscmservice@2.1',
	'com.qualcomm.qti.imscmservice@2.2',
	'com.qualcomm.qti.uceservice@2.0',
	'com.qualcomm.qti.uceservice@2.1',
	'com.qualcomm.qti.uceservice@2.2',
	'com.qualcomm.qti.uceservice@2.3',
	'vendor.qti.data.mwqem@1.0',
	'vendor.qti.data.slm@1.0',
	'vendor.qti.hardware.data.cne.internal.api@1.0',
	'vendor.qti.hardware.data.cne.internal.constants@1.0',
	'vendor.qti.hardware.data.cne.internal.server@1.0',
	'vendor.qti.hardware.data.dynamicdds@1.0',
	'vendor.qti.hardware.data.iwlan@1.0',
	'vendor.qti.hardware.data.latency@1.0',
	'vendor.qti.hardware.data.lce@1.0',
	'vendor.qti.hardware.data.qmi@1.0',
	'vendor.qti.hardware.mwqemadapter@1.0',
	'vendor.qti.hardware.slmadapter@1.0',
	'vendor.qti.latency@2.0',
	'vendor.qti.latency@2.1',
	'vendor.qti.hardware.data.connection@1.0',
	'vendor.qti.hardware.data.connection@1.1',
    ): lib_fixup_vendor_suffix,
    'libwpa_client': lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/camera/components/com.qti.node.watermark.so': blob_fixup()
        .add_needed('libpiex_shim.so'),
    'vendor/lib64/libwvhidl.so': blob_fixup()
        .add_needed('libcrypto_shim.so'),
    'vendor/lib64/mediadrm/libwvdrmengine.so': blob_fixup()
        .add_needed('libcrypto_shim.so'),
    'vendor/etc/wfdconfig.xml': blob_fixup()
        .regex_replace('<AudioStreamInSuspend>0</AudioStreamInSuspend>', '<AudioStreamInSuspend>1</AudioStreamInSuspend>')
        .regex_replace('<HID>0</HID>', '<HID>1</HID>'),
}  # fmt: skip

module = ExtractUtilsModule(
    'raphael',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
