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


    float rres = (v1.r + v2.r + v3.r + v4.r + v5.r + v6.r + v7.r + v8.r + v9.r)/9.0;
    float gres = (v1.g + v2.g + v3.g + v4.g + v5.g + v6.g + v7.g + v8.g + v9.g)/9.0;
    float bres = (v1.b + v2.b + v3.b + v4.b + v5.b + v6.b + v7.b + v8.b + v9.b)/9.0;

    
    vec4 final_color = vec4(rres, gres, bres, 1);
    
    gl_FragColor = clamp(abs(final_color), vec4(0,0,0,0), vec4(1,1,1,1));
}