varying vec2 pos;
uniform sampler2D s_texture;

void main() {
    float tx = pos.x;
    float ty = pos.y;

    float r;
    float g;
    float b;
    
    float y;
    float i;
    float q;

    vec4 v1 = texture2D(s_texture, vec2(tx, ty)).rgba;

    r = v1.r;
    g = v1.g;
    b = v1.b;

    y = 0.299*r + 0.587*g + 0.114*b;

    vec4 final_color = vec4(y, y, y, 1);
    
    gl_FragColor = final_color;
}