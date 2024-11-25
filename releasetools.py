#
# Copyright (C) 2019 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

import common

def FullOTA_InstallEnd(info):
  OTA_InstallEnd(info)
  return

def IncrementalOTA_InstallEnd(info):
  OTA_InstallEnd(info)
  return

def AddImage(info, dir, basename, dest):
  path = dir + "/" + basename
  if path not in info.input_zip.namelist():
    return

  data = info.input_zip.read(path)
  common.ZipWriteStr(info.output_zip, basename, data)
  info.script.AppendExtra('package_extract_file("%s", "%s");' % (basename, dest))

def FullOTA_InstallBegin(info):
  info.script.AppendExtra('ifelse(is_mounted("/system_root"),unmount("/system_root"));')
  info.script.AppendExtra('ifelse(is_mounted("/vendor"),unmount("/vendor"));')
  info.script.AppendExtra('assert(getprop("ro.boot.super_partition") == "system" || abort("ERROR: This recovery does not support retrofit dynamic partitions."););')
  info.script.AppendExtra('run_program("/system/bin/toybox", "blkdiscard", "/dev/block/bootdevice/by-name/system"); || abort("ERROR: Failed to discard data on system partition.");')
  info.script.AppendExtra('run_program("/system/bin/toybox", "blkdiscard", "/dev/block/bootdevice/by-name/vendor"); || abort("ERROR: Failed to discard data on vendor partition.");')
  info.script.AppendExtra('ui_print("- Flashing super_empty onto system partition...");')
  AddImage(info, "RADIO", "super_dummy.img", "/dev/block/bootdevice/by-name/system");
  return

def OTA_InstallEnd(info):
  info.script.Print("Patching device-tree and verity images...")
  AddImage(info, "IMAGES", "vbmeta.img", "/dev/block/bootdevice/by-name/vbmeta")
  return
