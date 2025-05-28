from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    original_images = ['Soldier.png', 'Soldier_with_tank.png']
    camo_designs = ['camo1.png', 'camo2.png', 'camo3.png', 'Camo4.png', 'Camo5.png', 'Camo6.png']
    output_path = None
    selected_original = None
    selected_camo = None

    if request.method == 'POST':
        selected_original = request.form.get('original_image')
        selected_camo = request.form.get('camo_design')
        base = 'soldier' if selected_original == 'Soldier.png' else 'soldier_with_tank'
        overlay_file = selected_camo.replace('.png', '_overlay.png')
        output_path = f"/static/images/output/{base}/{overlay_file}"

    return render_template("index.html",
                           original_images=original_images,
                           camo_designs=camo_designs,
                           output_path=output_path,
                           selected_original=selected_original,
                           selected_camo=selected_camo)

if __name__ == '__main__':
    app.run(debug=True)
