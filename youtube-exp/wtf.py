
import base64

yt_filters = {
"u-h":"upload:last hour",
"u-t":"uploaded:today",
"u-w":"uploaded:this week",
"u-m":"uploaded:this month",
"u-y":"uploaded:this year",
"t-v":"Type:video",
"t-c":"Type:channel",
"t-p":"Type:playlist",
"t-m":"Type:movie",
"t-s":"Type:show",
"d-s":"Duration:short",
"d-l":"Duration:long",
"f-live":"Features:live",
"f-4k":"Features:4k",
"f-hd":"Features:HD",
"f-s-cc":"Features:Subtitles/CC",
"f-cc":"Features:CreativeCommons",
"f-360":"Features:360°",
"f-180":"Features:vr180",
"f-3d":"Features:3d",
"f-hdr":"Features:HDR",
"f-l":"Features:Location",
"f-p":"Features:Purchased",
"s-re":"Sorted by:Relevance",
"s-ud":"Sorted by:Upload Date",
"s-vc":"Sorted by:View Count",
"s-ra":"Sorted by:Rating",
}

bdd = {
"t-v_s-re": "EgIQAQ==",
"u-h_t-v_s-re": "EgIIAQ==",
"u-t_t-v_s-re": "EgQIAhAB",
"u-w_t-v_s-re":"EgQIAxAB",
"u-h_t-v_d-s_s-re":"EgYIARABGAE=",
"u-t_t-v_d-s_s-re":"EgYIAhABGAE=",
"u-w_t-v_d-s_s-re":"EgYIAxABGAE=",
"u-h_t-v_d-s_f-live_s-re":"EggIARABGAFAAQ==",
"u-t_t-v_d-s_f-live_s-re":"EggIAhABGAFAAQ==",
"u-w_t-v_d-s_f-live_s-re":"EggIAxABGAFAAQ==",

}
def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

for filters,bs64values in bdd.items():
    filtersNames = filters.split("_")
    filters_formatted = list()
    for filter,name in yt_filters.items():
        for curr_filter in filtersNames:
            if curr_filter == filter:
                filters_formatted.append(name)
    filters_formatted = " ".join(filters_formatted)
    encoded = base64.decodebytes(bs64values.encode("ascii"))
    print("".join(["{:08b}".format(x) for x in encoded]), filters_formatted)
while True:
    inp = input('bs64 to bin> ')
    if str(inp) == "-1":
        break
    encoded = base64.decodebytes(inp.encode("ascii"))
    print("".join(["{:08b}".format(x) for x in encoded]))

while True:
    inp = input('bin to bs64> ')
    if str(inp) == "-1":
        break
    encoded = base64.encodebytes(bitstring_to_bytes(inp)).decode("ascii").strip()
    encoded = encoded.replace("=", "%253D")
    print("Encoded into bs64:", encoded)
