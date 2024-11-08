# coding=utf-8
import gradio as gr
import traceback


def hello_world_fn(username: str) -> tuple[str, str]:
    try:
        return f"HELLO WORLD\n{username.upper()}", "SUCCESS"
    except Exception as e:
        return f"opus! some exception {e}\n{traceback.format_exc()}", "FAILED"


def extract_p(html_input):
    # str_html = "<a>111<b>222</b><p>333<c>444</c></p><p>555</p></a>"
    str_html = html_input
    str_arr = str_html.split("<p>")

    return str_arr[1][:3] + "\n" + str_arr[2][:3], "SUCCESS"


def main() -> None:
    with gr.Blocks(title="DeepLang Data test project") as demo:
        with gr.Tab("hello world 0"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("hello world 1"):
            raw_input = gr.Textbox(lines=1, placeholder="输入你的名字(英文)", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")

            btn = gr.Button("开始转换")
            btn.click(
                fn=hello_world_fn,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

        with gr.Tab("html parser"):
            raw_input = gr.Textbox(lines=1, placeholder="输入html数据", label="")
            pack_output = gr.Textbox(label="输出")
            status_output = gr.Textbox(label="状态信息")
            btn = gr.Button("开始转换")
            btn.click(
                fn=extract_p,
                inputs=raw_input,
                outputs=[pack_output, status_output],
            )

    demo.queue(default_concurrency_limit=100).launch(
        inline=False,
        debug=False,
        server_name="127.0.0.1",
        server_port=8081,
        share=True,
        show_error=True,
    )


if __name__ == "__main__":
    main()
