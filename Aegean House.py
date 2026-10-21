from earsketch import *
setTempo(120)

clap = RD_TRAP_ARCADEFIRESFX_1
beatString = "00+-0-00+0-0+++"

# Main beat
fitMedia(RD_UK_HOUSE_MAINBEAT_8, 1, 1, 16)

# Tambourine
fitMedia(YG_RNB_TAMBOURINE_1, 3, 1, 30)

for measure in range(2, 5):
    fitMedia(FLORACARABITSIOS_BELL_GREECE2__BORQUE_2008__WAV, 2, 2, 3 + 1)

fitMedia(FLORACARABITSIOS_GREECE_NAXOS_CICADAS_1_WAV, 4, 3, 30)

fitMedia(AK_UNDOG_808_1, 5, 1, 16)

# Main house vocals 
fitMedia(COMMON_LOVE_VOX_ADLIB_1, 6, 4,6)

fitMedia(HOUSE_ACOUSTIC_PIANO_003, 7, 6, 60)

fitMedia(HOUSE_BREAKBEAT_022, 8, 6, 16)
# slice and rearrange by sixteenth notes 
slices = [1.0,1.375, 1.25, 1.5, 2.0, 2.25]
makeBeatSlice(IRCA_LATIN_JAZZ_1_PIANO_1, 9, 10, "4--04-0-30-10+30", slices)

fitMedia(HOUSE_BREAKBEAT_022, 8, 6, 16)
# slice and rearrange by sixteenth notes 
slices = [1.0,1.375, 1.25, 1.5, 2.0, 2.25]
makeBeatSlice(IRCA_LATIN_JAZZ_1_PIANO_1, 10, 11, "4--04-0-30-10+30", slices)

fitMedia(HOUSE_BREAKBEAT_022, 8, 6, 16)
# slice and rearrange by sixteenth notes 
slices = [1.0,1.375, 1.25, 1.5, 2.0, 2.25]
makeBeatSlice(IRCA_LATIN_JAZZ_1_PIANO_1, 11, 12, "4--04-0-30-10+30", slices)

fitMedia(FLORACARABITSIOS_BELL_GREECE2__BORQUE_2008__WAV, 12, 3, 4 + 1)

fitMedia(HOUSE_BREAKBEAT_022, 8, 6, 16)
# slice and rearrange by sixteenth notes 
slices = [1.0,1.375, 1.25, 1.5, 2.0, 2.25]
makeBeatSlice(IRCA_LATIN_JAZZ_1_PIANO_1, 11, 22, "4--04-0-30-10+30", slices)

fitMedia(HOUSE_BREAKBEAT_022, 8, 6, 16)
# slice and rearrange by sixteenth notes 
slices = [1.0,1.375, 1.25, 1.5, 2.0, 2.25]
makeBeatSlice(IRCA_LATIN_JAZZ_1_PIANO_1, 11, 24, "4--04-0-30-10+30", slices)

fitMedia(HOUSE_BREAKBEAT_022, 8, 1, 45)

fitMedia(FLORACARABITSIOS_MP3, 14, 20, 30)

fitMedia(FLORACARABITSIOS_GREECE_NAXOS_CICADAS_1_WAV, 15, 20, 21)
# slice and rearrange by sixteenth notes 
slices = [1.0, 1.375, 1.25, 1.5, 2.0, 2.25]
makeBeatSlice(FLORACARABITSIOS_GREECE_NAXOS_CICADAS_1_WAV, 15, 22, "4--04-0-30-10+30", slices)

fitMedia(FLORACARABITSIOS_MP3, 16, 22, 35)

# slice and rearrange by sixteenth notes 
slices = [1.0, 1.375, 1.25, 1.5, 2.0, 2.25]
makeBeatSlice(FLORACARABITSIOS_GREECE_NAXOS_CICADAS_1_WAV, 15, 25, "4--04-0-30-10+30", slices)

# slice and rearrange by sixteenth notes 
slices = [1.0, 1.375, 1.25, 1.5, 2.0, 2.25]
makeBeatSlice(FLORACARABITSIOS_GREECE_NAXOS_CICADAS_1_WAV, 15, 27, "4--04-0-30-10+30", slices)

# slice and rearrange by sixteenth notes 
slices = [1.0, 1.375, 1.25, 1.5, 2.0, 2.25]
makeBeatSlice(FLORACARABITSIOS_GREECE_NAXOS_CICADAS_1_WAV, 15, 29, "4--04-0-30-10+30", slices)

# slice and rearrange by sixteenth notes 
slices = [1.0, 1.375, 1.25, 1.5, 2.0, 2.25]
makeBeatSlice(FLORACARABITSIOS_GREECE_NAXOS_CICADAS_1_WAV, 15, 31, "4--04-0-30-10+30", slices)

fitMedia(HOUSE_ACOUSTIC_PIANO_003, 7, 30, 45)

# adding in greek music from taperecordings 
fitMedia(FLORACARABITSIOS_PAROS1, 17, 16, 24)

fitMedia(FLORACARABITSIOS_PAROS2, 17, 24, 30)

fitMedia(RD_UK_HOUSE_SOLODRUMPART_1, 18, 30, 60)

fitMedia(FLORACARABITSIOS_BELL_GREECE2__BORQUE_2008__WAV, 12, 30, 31 + 1)

fitMedia(AK_UNDOG_808_1, 5, 30, 60)

fitMedia(YG_RNB_TAMBOURINE_1, 3, 35, 60)

fitMedia(RD_UK_HOUSE_MAINBEAT_8, 1, 35, 60)

fitMedia(HOUSE_BREAKBEAT_012, 19, 36, 60)

# Fills
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(IRCA_OS_BONGO_HIGH_OPEN, 20, 35, fillA)

# Fills
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(IRCA_OS_BONGO_HIGH_OPEN, 20, 45, fillA)

# Fills
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(IRCA_OS_BONGO_HIGH_OPEN, 20, 47, fillA)

# Fills
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(IRCA_OS_BONGO_HIGH_OPEN, 20, 49, fillA)

# Fills
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(IRCA_OS_BONGO_HIGH_OPEN, 20, 51, fillA)

# Fills
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(IRCA_OS_BONGO_HIGH_OPEN, 20, 53, fillA)

# Fills
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(IRCA_OS_BONGO_HIGH_OPEN, 20, 55, fillA)

# Fills
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(IRCA_OS_BONGO_HIGH_OPEN, 20, 57, fillA)

# Fills
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(IRCA_OS_BONGO_HIGH_OPEN, 20, 59, fillA)

# Fills Greek sound
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(FLORACARABITSIOS_GREECE_NAXOS_CICADAS_1_WAV, 21, 46, fillA)

# Fills Greek sound
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(FLORACARABITSIOS_GREECE_NAXOS_CICADAS_1_WAV, 21, 48, fillA)

# Fills Greek sound
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(FLORACARABITSIOS_GREECE_NAXOS_CICADAS_1_WAV, 21, 50, fillA)

# Fills Greek sound
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(FLORACARABITSIOS_GREECE_NAXOS_CICADAS_1_WAV, 21, 52, fillA)

# Fills Greek sound
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(FLORACARABITSIOS_GREECE_NAXOS_CICADAS_1_WAV, 21, 54, fillA)

# Fills Greek sound
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(FLORACARABITSIOS_GREECE_NAXOS_CICADAS_1_WAV, 21, 56, fillA)

# Fills Greek sound
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(FLORACARABITSIOS_GREECE_NAXOS_CICADAS_1_WAV, 21, 58, fillA)

#adding Greek speech saying cheers 
fitMedia(FLORACARABITSIOS_UVA, 22, 37, 39)

#remixed sound from Paros vocals using a loop
for measure in range(40, 60, 2):
    fitMedia(FLORACARABITSIOS_UVA2, 23, measure, measure + 1)

