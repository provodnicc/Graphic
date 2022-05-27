varying vec2 pos;
uniform sampler2D s_texture;

void main() {
    float tx = pos.x;
    float ty = pos.y;
    float r;
    float g;
    float b;
    float i;
    float y;

    vec4 v1 = texture2D(s_texture, vec2(tx, ty)).rgba;

                r = v1.r;
                g = v1.g;
                b = v1.b;

    // i = 0.596*r - 0.274*g - 0.322*b;

    y = 0.299*r + 0.587*g + 0.114*b;
    i = (y/255.0)*255.0;

    if(i<=0.33){
        r = 255.0;
        g = 0.0;
        b = 0.0;
    }else if((i>0.33)&&(i<=0.66)){
        r = 0.0;
        g = 255.0;
        b = 0.0;    
    }else{
        r = 0.0;
        g = 0.0;
        b = 255.0;
    }


    gl_FragColor = vec4(r, g, b, 1);
}