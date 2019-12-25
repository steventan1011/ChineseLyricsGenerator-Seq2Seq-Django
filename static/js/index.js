function download() {
    keywords = $("#keywords").text();
    singer = $("#singer").text();
    likely_extent = $('likely_extent').text();
    download_content = ["关键词：", keywords, "\n\n", "歌手：", singer, "\n\n", "相似度：", "\n\n", "生成歌词：\n"];
    $("#lyrics_content p").each(function (i, value) {
        download_content.push($(this).text() + "\n");
    });
    console.log(content);
    // 创建下载链接
    var download_link = document.createElement('a');
    download_link.download = 'lyrics.txt';
    download_link.style.display = 'none';
    // 下载内容
    // 字符内容转变成blob地址
    var blob = new Blob(download_content, {
        type: "text/plain"
    });
    download_link.href = URL.createObjectURL(blob);
    // 触发点击
    document.body.appendChild(download_link);
    download_link.click();
    // 然后移除
    document.body.removeChild(download_link);
}

singer_res = {
    "zhoujielun": "周杰伦",
    "dengziqi": "邓紫棋",
    "zhangshaohan": "张韶涵",
    "tenggeer": "腾格尔",
    "zhangjie": "张杰"
};

layui.use(['form', 'rate', 'slider'], function () {
    var form = layui.form;
    var rate = layui.rate;
    var $ = layui.$;
    var slider = layui.slider;

    generate_length = 7;
    likely_extent = '推荐';

    slider.render({
        elem: '#likely',
        min:0,
        max:100,
        value: 50,
        step: 25,
        theme: '#1E9FFF',
        tips: true,
        showstep: true,
        setTips: function (value) {
            return_text = ''
            switch (value) {
                case 0:
                    return_text = '最不相似';
                    break
                case 25:
                    return_text = '很不相似';
                    break
                case 50:
                    return_text = '推荐';
                    break
                case 75:
                    return_text = '很相似';
                    break
                default:
                    return_text = '最相似';
            };
            return return_text;
        },
        change: function (value) {
            $('#test-slider-likely').html('相似程度：' + value);
            likely_extent = value;
        }
    });

    rate.render({
        elem: '#length_rate',
        value: generate_length,
        length: 10,
        text: true,
        setText: function (value) {
            this.span.text(value + "句");
        },
        choose: function (value) {
            generate_length = value;
        }
    });

    // 表单提交
    form.on('submit(form_submit)', function (data) {
        submit_data = data.field;
        submit_data['generate_length'] = generate_length;
        submit_data['likely_extent'] = likely_extent;
        console.log(submit_data);
        $.ajax({
            url: '/search',
            data: submit_data,
            dataType: 'json',
            type: 'GET',
            success: function (response) {
                var keywords = response['keywords'].join("、");
                console.log(response['content']);
                $("#keywords").text(keywords);
                $('#generate_length').text(response['generate_length']);
                $('#singer').text(singer_res[response['singer']]);
                var content_html = ''
                for (var lyrics of response['content']) {
                    this_sentence = '<p>' + lyrics + '</p>';
                    content_html += this_sentence;
                }
                $('#lyrics_content').html(content_html);
                $('#likely_extent').text(response['likely_extent']);
            }
        });
        return false;
    });
});