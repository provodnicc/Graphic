varying vec2 pos;
uniform sampler2D s_texture;
uniform float texture_width;
uniform float texture_height;

void main() {
    float tx = pos.x;
    float ty = pos.y;
    float dx = 1.0 / texture_width;
    float dy = 1.0 / texture_height;
    
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

    
    

    vec4 v1 = texture2D( s_texture, vec2( tx, ty ) + vec2( -dx, -dy ) );
    vec4 v2 = texture2D( s_texture, vec2( tx, ty ) + vec2( -dx, 0 ) );
    vec4 v3 = texture2D( s_texture, vec2( tx, ty ) + vec2( -dx, dy ) );
    vec4 v4 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0, -dy ) );
    vec4 v5 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0 , 0 ) );
    vec4 v6 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0, dy ) );
    vec4 v7 = texture2D( s_texture, vec2( tx, ty ) + vec2( dx, -dy ) );
    vec4 v8 = texture2D( s_texture, vec2( tx, ty ) + vec2( dx, 0 ) );
    vec4 v9 = texture2D( s_texture, vec2( tx, ty ) + vec2( dx, dy ) );

    float 1_gray = v1.r*0.299 + v1.g*0.587 + v1.b*0.114;
    float 2_gray = v2.r*0.299 + v2.g*0.587 + v2.b*0.114;
    float 3_gray = v3.r*0.299 + v3.g*0.587 + v3.b*0.114;
    float 4_gray = v4.r*0.299 + v4.g*0.587 + v4.b*0.114;
    float 5_gray = v5.r*0.299 + v5.g*0.587 + v5.b*0.114;
    float 6_gray = v6.r*0.299 + v6.g*0.587 + v6.b*0.114;
    float 7_gray = v7.r*0.299 + v7.g*0.587 + v7.b*0.114;
    float 8_gray = v8.r*0.299 + v8.g*0.587 + v8.b*0.114;
    float 9_gray = v9.r*0.299 + v9.g*0.587 + v9.b*0.114;


    vec4 v1_gray = vec4(1_gray, 1_gray, 1_gray, 1);
    vec4 v2_gray = vec4(2_gray, 2_gray, 2_gray, 1);
    vec4 v3_gray = vec4(3_gray, 3_gray, 3_gray, 1);
    vec4 v4_gray = vec4(4_gray, 4_gray, 4_gray, 1);
    vec4 v5_gray = vec4(5_gray, 5_gray, 5_gray, 1);
    vec4 v6_gray = vec4(6_gray, 6_gray, 6_gray, 1);
    vec4 v7_gray = vec4(7_gray, 7_gray, 7_gray, 1);
    vec4 v8_gray = vec4(8_gray, 8_gray, 8_gray, 1);
    vec4 v9_gray = vec4(9_gray, 9_gray, 9_gray, 1);

    vec4 color_start = (   v1_gray*-1 + v2_gray*0 + v3_gray*1
                         + v4_gray*-1 + v5_gray*0 + v6_gray*1 
                         + v7_gray*-1 + v8_gray*0 + v9_gray*1);
    gl_FragColor = clamp(abs(v5 - final_color) * 100.0, vec4(0,0,0,0), vec4(1,1,1,1));
}