import re;

def prepare(s): # tien xu lo xau
    for i in range(0,len(s)):
        s[i] = re.sub("%|:|'|@|#|\$|\,|\"|\(|\)|&|\*|Nguồn.*|[0-9]|\/|\.|\“|’|;| - |\]|\[" , '',s[i])
        s[i] = re.sub("[\t]|  | | - ", " ",s[i])


s="Bầu_Đệ   cán_bộ công_chức chỉ ngồi bói chữ  Ông Nguyễn_Văn_Đệ đã có những chia_sẻ thẳng_thắn về vấn_đề tổ_chức cán_bộ công_chức và nhận được sự hưởng_ứng của hàng nghìn đại_biểu tham_dự Hội_nghị đối_tho"

s=s.split("\n")

prepare(s)
s[0].strip("")

print(s)