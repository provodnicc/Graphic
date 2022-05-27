varying vec2 pos;
uniform sampler2D s_texture;
uniform float texture_width;
uniform float texture_height;

void main() {
    float tx = pos.x;
    float ty = pos.y;
    float dx = 1.0 / texture_width;
    float dy = 1.0 / texture_height;


    vec4 v1 = texture2D( s_texture, vec2( tx, ty ) + vec2( -dx, -dy ) ).rgba;
    vec4 v2 = texture2D( s_texture, vec2( tx, ty ) + vec2( -dx, 0 ) ).rgba;
    vec4 v3 = texture2D( s_texture, vec2( tx, ty ) + vec2( -dx, dy ) ).rgba;
    vec4 v4 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0, -dy ) ).rgba;
    vec4 v5 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0 , 0 ) ).rgba;
    vec4 v6 = texture2D( s_texture, vec2( tx, ty ) + vec2( 0, dy ) ).rgba;
    vec4 v7 = texture2D( s_texture, vec2( tx, ty ) + vec2( dx, -dy ) ).rgba;
    vec4 v8 = texture2D( s_texture, vec2( tx, ty ) + vec2( dx, 0 ) ).rgba;
    vec4 v9 = texture2D( s_texture, vec2( tx, ty ) + vec2( dx, dy ) ).rgba;
    
    
    vec4 final_color;


    float gray_1 = v1.r*0.299 + v1.g*0.587 + v1.b*0.114;
    float gray_2 = v2.r*0.299 + v2.g*0.587 + v2.b*0.114;
    float gray_3 = v3.r*0.299 + v3.g*0.587 + v3.b*0.114;
    float gray_4 = v4.r*0.299 + v4.g*0.587 + v4.b*0.114;
    float gray_5 = v5.r*0.299 + v5.g*0.587 + v5.b*0.114;
    float gray_6 = v6.r*0.299 + v6.g*0.587 + v6.b*0.114;
    float gray_7 = v7.r*0.299 + v7.g*0.587 + v7.b*0.114;
    float gray_8 = v8.r*0.299 + v8.g*0.587 + v8.b*0.114;
    float gray_9 = v9.r*0.299 + v9.g*0.587 + v9.b*0.114;


    if((gray_1 >= 0.85)||(gray_2 >= 0.85)||(gray_3 >= 0.85)||(gray_4 >= 0.85)||(gray_5 >= 0.85)||(gray_6 >= 0.85)||(gray_7 >= 0.85)||(gray_8 >= 0.85)||(gray_9 >= 0.85)){
        final_color = vec4(1.0, 1.0, 1.0, 1);
    }
    else{
        final_color = vec4(0.0, 0.0, 0.0, 1);
    }
    
    gl_FragColor = clamp(abs(final_color), vec4(0,0,0,0), vec4(1,1,1,1));
}